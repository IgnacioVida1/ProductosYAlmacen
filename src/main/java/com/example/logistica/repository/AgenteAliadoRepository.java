package com.example.logistica.repository;

import com.example.logistica.entity.AgenteAliado;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface AgenteAliadoRepository extends JpaRepository<AgenteAliado, Long> {
}
